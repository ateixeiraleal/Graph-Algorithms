<div class="header">
    <span>URI Online Judge | 1209</span>
    <h1>St. Petersburg Parties</h1>
    <div><p>
	    By Marcio T. I. Oshiro, USP <img alt="" src="https://resources.urionlinejudge.com.br/gallery/images/flags/br.gif" style="width: 16px; height: 11px; " /> Brazil</p>
    </div>
    <strong>Timelimit: 3</strong>
</div>
<div class="problem">
    <div class="description">
		<p>
			St. Petersburg became after the end of the Iron Curtain in the early '90s, one of the main cities of the alternative scene worldwide. Groups
			of punks, hardcore bands and several other representatives of the alternative scene moved to the city, attracted by the large amount of young
			people. With the emergence of virtual communities, a few years later, it was noted the enormous potential of using these communities to combine
			meetings, parties, raves, etc..
		</p>
		<p>
			In these celebrations of St. Petersburg is always very important that each participant has at least a certain number of friends on the social
			network. At the same time, we want to invite as many people as possible to St. Petersburg since the restriction on the number of friends is
			satisfied. This constraint says that, to be invited to the party, the person must have at least one number <strong>K</strong> of friends on
			the guest list.
		</p>
		<p>
			Your task in this problem is, given the number of people in the community and to list their relationships, determine what should be called
			to the party that has the largest possible number of participants satisfying the constraint.
		</p>
	</div>
	<h2>Input</h2>
	<div class="input">
		<p>
			The input have many test cases and ends with the end of file (EOF). The first line of each test case contains three integers <strong>N</strong>
			(1 ≤ <strong>N</strong> ≤ 1000), <strong>M</strong> and <strong>K</strong>&nbsp;(O ≤ <strong>K</strong> ≤ <strong>N</strong>) representing
			respectively the number of people in the community, the number of friendships in this community and the minimum number of friends asked a
			person must have to be invited. Each person in the community is identified by numbers from 1 to <strong>N</strong>. Each of the next
			<strong>M</strong> lines of the test case contains a pair of people indicating that they are friends in the social network.
		</p>
	</div>
	<h2>Output</h2>
	<div class="output">
		<p>
			For each test case print a single line containing the list of people to invite separated by a blank space. The list should be sorted in
			ascending order. If anyone can be invited, print the number 0.
		</p>
	</div>
	<div class="both"></div>
	<table>
		<thead>
			<tr>
				<td>Sample Input</td>
				<td>Sample Output</td>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td class="division">
					<p>
						6 6 2<br />
						1 3<br />
						3 5<br />
						2 3<br />
						2 4<br />
						4 6<br />
						6 2<br />
						6 6 3<br />
						1 2<br />
						2 3<br />
						3 1<br />
						4 5<br />
						5 6<br />
						6 4
					</p>
                </td>
				<td>
					<p>
						2 4 6<br />
						0
					</p>
				</td>
			</tr>
		</tbody>
	</table>
	<p class="footer">
		XVI Maratona de Programação IME-USP, 2012. Special thanks to Carlos E. Ferreira.
	</p>
</div>